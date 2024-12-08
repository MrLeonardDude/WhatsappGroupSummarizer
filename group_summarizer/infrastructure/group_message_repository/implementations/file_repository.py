from os import getenv
from typing import List, Optional
from re import compile 

from group_summarizer.infrastructure.group_message_repository.interface import GroupMessageRepository 
from group_summarizer.domain.group_message import GroupMessage
from group_summarizer.domain.group_member import GroupMember

IS_START_MESSAGE_REGEX = r"\d\d?\/\d\d?\/\d\d.*"
REGEX = compile(IS_START_MESSAGE_REGEX)


class FileRepository(GroupMessageRepository):
    
    def __enter__(self):
        filename = getenv('DUMP_FILE_NAME', '')
        self.__file_reader = open(filename, 'r')
        return self

    def __read_message(self) -> Optional[str]:
        unformatted_msg = self.__file_reader.readline()
        
        if not unformatted_msg:
            return None

        while True:
            fp_checkpoint = self.__file_reader.tell()
            new_line = self.__file_reader.readline()
            
            if not new_line:
                return unformatted_msg
            
            if REGEX.match(new_line) is not None:
                self.__file_reader.seek(fp_checkpoint)
                break
                
            unformatted_msg += new_line
            
        return unformatted_msg

    def get_messages(self) -> Optional[GroupMessage]:
        while True:
            unformatted_message = self.__read_message()
                
            if not unformatted_message:
                return None
            
            msg_date, unformatted_message = unformatted_message.split(',', 1)
            msg_hour, unformatted_message = unformatted_message.split('-', 1)
            if ': ' not in unformatted_message:
                yield GroupMessage(GroupMember('0', 'WppAdmin'), unformatted_message, msg_date)
                continue
            msg_name, formatted_message = unformatted_message.split(': ', 1)
            
            yield GroupMessage(GroupMember('', msg_name.replace(' ', '', 1)), formatted_message.replace('\n', ''), msg_date)
    
    def __exit__(self, exc_type, exc_value, exc_tb): 
        self.__file_reader.close()

from dotenv import load_dotenv
load_dotenv()

from group_summarizer.infrastructure.group_message_repository.implementations.file_repository import FileRepository
from group_summarizer.use_cases.list_messages import list_messages


if __name__ == '__main__':
    with FileRepository() as group_file_repository:
        list_messages(group_file_repository)


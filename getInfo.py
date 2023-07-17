from src.ticket import Ticket


def get_info(file_name):
    result = {}
    pdf_file = Ticket(file_name)
    result["Data"] = pdf_file.parsing_file(True)
    result["Metainfo"] = pdf_file.get_metadata
    return result


print(get_info("test_task.pdf"))

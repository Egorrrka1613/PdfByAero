import fitz

from util.helper import get_path_to_file


def update_parsed_data(span, extracted_info: dict, key) -> None:
    origin = span["origin"]

    extracted_info.update(
        {
            key: {
                "Размер шрифта": int(span["size"]),
                "Шрифт": span["font"],
                "Цвет шрифта": span["color"],
                "Флаги (формат шрифта)": span["flags"],
                "Точка отсчета": tuple(int(num) for num in origin),
            }
        }
    )


class Ticket:
    def __init__(self, file_name: str):
        self.path = get_path_to_file(file_name)

    def parsing_file(self, need_values_data: bool = False) -> dict:
        with fitz.open(self.path) as doc:
            result = {}
            for page in doc:
                text = page.get_text("dict")
                for block in text["blocks"]:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            if need_values_data:
                                key = span["text"]
                                update_parsed_data(span, result, key)
                            else:
                                if block == text["blocks"][0]:
                                    update_parsed_data(span, result, span["text"])
                                elif ":" in span["text"]:
                                    key, value = span["text"].split(":")
                                    update_parsed_data(span, result, key)

            return result

    @property
    def get_metadata(self) -> dict:
        result = {}
        with fitz.open(self.path) as doc:
            result["Metadata"] = doc.metadata
        return result

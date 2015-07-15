from . import documents


def extract_raw_text_from_element(element):
    if isinstance(element, documents.Text):
        return element.value
    else:
        text = "".join(map(extract_raw_text_from_element, element.children))
        if isinstance(element, documents.Paragraph):
            return text + "\n\n"
        else:
            return text

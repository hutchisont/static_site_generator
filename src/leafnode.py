from htmlnode import HTMLNode


class LeafNode(HTMLNode):

    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 props: dict[str, str] = None
                 ):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("It is required for leaf nodes to have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

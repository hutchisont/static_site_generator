class HTMLNode:
    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 children: list = None,
                 props: dict[str, str] = None
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for key, val in self.props.items():
            html += f" {key}=\"{val}\""
        return html

    def __repr__(self):
        return f"""tag: {self.tag}
value: {self.value}
children: {self.children}
props: {self.props}"""


class LeafNode(HTMLNode):

    def __init__(self,
                 tag: str,
                 value: str,
                 props: dict[str, str] = None
                 ):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("It is required for leaf nodes to have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"""tag: {self.tag}
value: {self.value}
props: {self.props}"""


class ParentNode(HTMLNode):

    def __init__(self,
                 tag: str,
                 children: list,
                 props: dict[str, str] = None
                 ):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"
        return html

    def __repr__(self):
        return f"""tag: {self.tag}
children: {self.children}
props: {self.props}"""

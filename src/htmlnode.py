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
props: {self.props}
        """

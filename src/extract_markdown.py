from blocks import block_to_block_type, BlockType
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from split import (
    text_to_textnodes,
    extract_markdown_images,
    extract_markdown_links
)


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue

        lines = block.split("\n")
        cleaned_lines = []
        for line in lines:
            cleaned_lines.append(line.strip())


        block = "\n".join(cleaned_lines).strip()

        if block != "":
            filtered_blocks.append(block)
    return filtered_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.QUOTE:
        return create_quote_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return create_ulist_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return create_olist_node(block)
    if block_type == BlockType.CODE:
        return create_code_node(block)
    if block_type == BlockType.HEADING:
        return create_heading_node(block)
    return create_paragraph_node(block)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def create_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def create_heading_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block) or block[level] != " ":
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children) 

def create_code_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def create_quote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith("> "):
            raise ValueError("Invalid quote block")
        new_lines.append(line[2:])
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def create_ulist_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)

def create_olist_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line[line.find(". ") + 2 :]
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)
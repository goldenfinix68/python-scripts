import re

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def parse_blocks(content):
    blocks = re.split(r'\n(?=\d+\.)', content)  # Split based on the pattern "{Number}."
    block_dict = {}

    for block in blocks:
        id_match = re.search(r'ID\s*-\s*(\S+)', block)
        if id_match:
            block_id = id_match.group(1)
            block_dict[block_id] = block.strip()

    return block_dict

def compare_blocks(blocks1, blocks2):
    only_in_first = {k: v for k, v in blocks1.items() if k not in blocks2}
    only_in_second = {k: v for k, v in blocks2.items() if k not in blocks1}
    
    return only_in_first, only_in_second

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def prepare_content(blocks):
    content = []
    for id, block in blocks.items():
        content.append(f"ID: {id}\n{block}\n")
    return "\n".join(content)


# Read the documents
content1 = read_file('Medline.txt')
content2 = read_file('Medline2.txt')

# Parse the documents
blocks1 = parse_blocks(content1)
blocks2 = parse_blocks(content2)

# Compare the blocks
only_in_first, only_in_second = compare_blocks(blocks1, blocks2)

# Prepare content for output
only_in_first_content = prepare_content(only_in_first)
only_in_second_content = prepare_content(only_in_second)

# Write the differences to three separate files
write_to_file('only_in_first.txt', only_in_first_content)
write_to_file('only_in_second.txt', only_in_second_content)

keys1 = list(only_in_first.keys())
print("Number of blocks in 'only_in_first.txt':", len(keys1))

keys2 = list(only_in_second.keys())
print("Number of blocks in 'only_in_second.txt':", len(keys2))
print("Differences written to 'only_in_first.txt' and 'only_in_second.txt'")

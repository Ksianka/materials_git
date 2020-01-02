from extract_data import extracted_data

from mdutils.mdutils import MdUtils

mdFile = MdUtils(file_name='Materials', title='Материалы по анализу данных')

topics = list(extracted_data.keys())


def create_table(topic_index):
    '''
    function to create table with extracted data for topic
    '''
    mdFile.new_header(level=1, title=topics[topic_index])    # style is set 'atx' format by default.

    list_of_headers = extracted_data[topics[topic_index]][0]
    n_of_columns = len(list_of_headers)
    for x in extracted_data[topics[topic_index]][1:]:
        for i in range(len(x)):
            list_of_headers.extend([str(x[i])])
    mdFile.new_line()
    n_of_rows = len(extracted_data[topics[topic_index]])
    mdFile.new_table(columns=n_of_columns, rows=n_of_rows, text=list_of_headers, text_align='center')

    mdFile.new_paragraph()


for index in range(len(topics)):
    try:
        create_table(index)
    except:
        print('Failed topic ' + topics[index])


# Create a table of contents
mdFile.new_table_of_contents(table_title='Содержание', depth=2)

mdFile.create_md_file()

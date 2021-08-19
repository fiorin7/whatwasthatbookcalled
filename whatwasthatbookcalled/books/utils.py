fields_per_page = {
    "__all__": 2,
    "title_tips": 1,
    "author_tips": 1,
    "language": 1,
    "year_written": 2,
    "year_read": 2,
    "part_of_serie": 2,
    "cover_description": 2,
    "genre": 3,
    "plot_details": 3,
    "quotes": 3,
    "additional_notes": 3,
}


def get_first_error_page(errors):
    first_field = list(errors.keys())[0]
    return fields_per_page[first_field]

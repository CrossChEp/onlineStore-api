def clear_model(model) -> dict:
    """clears pydantic model from null fields

    :param model: BaseModel
    :return: dict
    """
    clear_dict = {}
    for key, value in model.dict().items():
        if not value:
            continue
        clear_dict[key] = value
    return clear_dict

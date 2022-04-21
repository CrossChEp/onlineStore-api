def clear_model(model) -> dict:
    clear_dict = {}
    for key, value in model.dict().items():
        if not value:
            continue
        clear_dict[key] = value
    return clear_dict

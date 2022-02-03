def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    output = {"categories": []}
    for category_id in mapping['categoryIdsSorted']:
        category = mapping['categories'][category_id]
        items = []
        for role_id in category['roleIds']:
            role = mapping['roles'][role_id]
            items.append({"id": role['id'], "text": role['name']})
        new_category = {"id": f"category-{category['id']}", "text": category['name'], 'items': items}
        output['categories'].append(new_category)
    return output

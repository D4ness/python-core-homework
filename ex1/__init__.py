from mapping import RAW_MAPPING
# from pprint import pprint
def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    output = {"categories": []}
    # for category in mapping['categories'].values():
    for category_id in mapping['categoryIdsSorted']:
        category = mapping['categories'][category_id]
        items = []
        for role_id in category['roleIds']:
            role = mapping['roles'][role_id]
            # print({"id": role['id'], "text": role['name']})
            items.append({"id": role['id'], "text": role['name']})
        new_category = {"id": f"category-{category['id']}", "text": category['name'], 'items': items}
        # print(new_category)
        output['categories'].append(new_category)
    return output


# pprint(build_roles_tree(RAW_MAPPING))
# output = {}



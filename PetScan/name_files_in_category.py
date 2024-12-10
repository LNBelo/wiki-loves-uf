# -*- coding: utf-8 -*-
import requests


def request_petscan(category, depth, ):
    """Get name files in a category from Wikimedia Commons"""
    url = 'https://petscan.wmflabs.org/'
    parameters = {
        'language': 'commons',
        'project': 'commons',
        'depth': depth,
        'categories': category,
        'combination': 'subset',
        'negcats': '',
        'ns[6]': '1',  # in Page properties select File
        'larger': '',
        'smaller': '',
        'since_rev0': '',
        'minlinks': '',
        'maxlinks': '',
        'before': '',
        'after': '',
        'max_age': '',
        'show_redirects': 'both',
        'show_soft_redirects': 'both',
        'show_disambiguation_pages': 'both',
        'edits[bots]': 'both',
        'edits[anons]': 'both',
        'edits[flagged]': 'both',
        'page_image': 'any',
        'ores_type': 'any',
        'ores_prob_from': '',
        'ores_prob_to': '',
        'ores_prediction': 'any',
        'templates_yes': '',
        'templates_any': '',
        'templates_no': '',
        'outlinks_yes': '',
        'outlinks_any': '',
        'outlinks_no': '',
        'links_to_all': '',
        'links_to_any': '',
        'links_to_no': '',
        'sparql': '',
        'manual_list': '',
        'manual_list_wiki': '',
        'pagepile': '',
        'search_query': '',
        'search_wiki': '',
        'search_max_results': '500',
        'wikidata_source_sites': '',
        'namespace_conversion': 'keep',
        'subpage_filter': 'either',
        'common_wiki': 'auto',
        'common_wiki_other': '',
        'source_combination': '',
        'wikidata_item': 'no',
        'wikidata_label_language': '',
        'wikidata_prop_item_use': '',
        'wpiu': 'any',
        'sitelinks_yes': '',
        'sitelinks_any': '',
        'sitelinks_no': '',
        'min_sitelink_count': '',
        'max_sitelink_count': '',
        'labels_yes': '',
        'cb_labels_yes_l': '1',
        'langs_labels_yes': '',
        'labels_any': '',
        'cb_labels_any_l': '1',
        'langs_labels_any': '',
        'labels_no': '',
        'cb_labels_no_l': '1',
        'langs_labels_no': '',
        'format': 'json',
        'output_compatability': 'catscan',
        'sortby': 'none',
        'sortorder': 'ascending',
        'regexp_filter': '',
        'search_filter': '',
        'min_redlink_count': '1',
        'output_limit': '',
        'doit': 'Do it!',
        'referrer_url': '',
        'referrer_name': '',
        'interface_language': 'en',
        'active_tab': 'tab_pageprops'
    }
    r = requests.get(url, params=parameters)
    data = r.json()
    values = data['*'][0]["a"]["*"]

    for value in values:
        file = value["title"]

        with open('output.txt', 'a') as output:
            output.write(f'{category}\tFile:{file}\n')


if __name__ == "__main__":
    with open('output.txt', 'w') as output:
        output.write('')
    with open('input.txt') as entry:
        categories = entry.readlines()

    i = 1
    n = len(categories)
    for category in categories:
        category = category.strip()
        request_petscan(category, 2)
        print(f'{i}/{n}')
        i += 1

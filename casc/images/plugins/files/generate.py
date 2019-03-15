import xml.etree.ElementTree as etree


with open('plugins.xml') as plugins_file:
    plugins_data = plugins_file.read()

tree = etree.fromstring(plugins_data)

plugins = {}

for element in tree:
    plugin_name = element.find('shortName').text

    inverse_dependencies = plugins.get(plugin_name, {}).get('inverse_dependencies', [])

    plugins[plugin_name] = {
        'inverse_dependencies': inverse_dependencies,
        'dependencies': [],
        'version': element.find('version').text,
        'active': element.find('active').text,
        'deleted': element.find('deleted').text,
        'enabled': element.find('enabled').text,
    }

    for dependency in element.findall('dependency'):
        dependency_name = dependency.find('shortName').text

        if dependency_name not in plugins:
            plugins[dependency_name] = {'inverse_dependencies': []}

        plugins[dependency_name]['inverse_dependencies'].append(plugin_name)
        plugins[plugin_name]['dependencies'].append(dependency_name)

plugins_name = list(plugins.keys())
plugins_name.sort()

with open('/usr/local/jenkins/plugins.txt', 'w') as plugins_file:
    plugins_file.write('# Main plugins\n')
    for plugin_name in plugins_name:
        plugin_value = plugins[plugin_name]
        if not plugin_value['inverse_dependencies']:
            plugins_file.write('{name}:{version}\n'.format(name=plugin_name, version=plugin_value['version']))

    plugins_file.write('\n# Additional plugins\n')
    for plugin_name in plugins_name:
        plugin_value = plugins[plugin_name]
        if plugin_value['inverse_dependencies']:
            full_plugin_name = '{name}:{version}'.format(name=plugin_name, version=plugin_value['version'])
            plugins_file.write(f'{full_plugin_name:40} # via ')
            plugins_file.write(', '.join(plugin_value['inverse_dependencies']))
            plugins_file.write('\n')

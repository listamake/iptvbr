import xml.etree.ElementTree as ET

# Dados dos canais e informações relacionadas (exemplo)
channel_data = [
    {
        "id": "anitv.br",
        "display_name": "Locomotion SD",
        "url_tvg": "https://raw.githubusercontent.com/listamake/iptvbr/main/guide/Ch/geekdot.xml",
        "icon_url": "http://example.com/channel1.png"
    },
    {
        "id": "2",
        "display_name": "Canal 2",
        "url_tvg": "http://example.com/epg2.xml",
        "icon_url": "http://example.com/channel2.png"
    },
    # Mais canais...
]

# Criar o elemento raiz <tv>
tv = ET.Element("tv")

# Percorrer os dados dos canais
for channel_info in channel_data:
    channel_id = channel_info["id"]
    display_name = channel_info["display_name"]
    url_tvg = channel_info["url_tvg"]
    icon_url = channel_info["icon_url"]

    # Criar o elemento <channel> com o atributo id
    channel = ET.SubElement(tv, "channel")
    channel.set("id", channel_id)

    # Criar o elemento <display-name> e preencher com o nome do canal
    display_name_elem = ET.SubElement(channel, "display-name")
    display_name_elem.text = display_name

    # Criar o elemento <url-tvg> e preencher com a URL do EPG
    url_tvg_elem = ET.SubElement(channel, "url-tvg")
    url_tvg_elem.text = url_tvg

    # Criar o elemento <icon> com o atributo src e preencher com a URL do ícone
    icon_elem = ET.SubElement(channel, "icon")
    icon_elem.set("src", icon_url)

# Criar o objeto XML e adicionar o elemento raiz <tv>
epg_xml = ET.ElementTree(tv)

# Salvar o objeto XML em um arquivo
epg_xml.write("epgnew.xml", encoding="utf-8", xml_declaration=True)

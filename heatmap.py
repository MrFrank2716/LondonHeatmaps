import livepopulartimes
import folium
from folium.plugins import HeatMap

# List of Zone 1 stations with addresses
stations_with_addresses = {
    "Aldgate": "Aldgate Station, Aldgate High St, London EC3N 1AH, UK",
    "Aldgate East": "Aldgate East Station, Whitechapel High St, London E1 7PT, UK",
    "Angel": "Angel Station, Islington High St, London N1 9LQ, UK",
    "Baker Street": "Baker Street Station, Marylebone Rd, London NW1 5LA, UK",
    "Bank": "Bank Station, Princes St, London EC3V 3LA, UK",
    "Barbican": "Barbican Station, Aldersgate St, London EC1A 4JA, UK",
    "Bayswater": "Bayswater Station, Queensway, London W2 4RH, UK",
    "Blackfriars": "Blackfriars Station, Queen Victoria St, London EC4V 4DY, UK",
    "Bond Street": "Bond Street Station, Oxford St, London W1C 2JH, UK",
    "Borough": "Borough Station, Borough High St, London SE1 1JX, UK",
    "Cannon Street": "Cannon Street Station, Cannon St, London EC4N 6AP, UK",
    "Chancery Lane": "Chancery Lane Station, High Holborn, London WC1V 6DR, UK",
    "Charing Cross": "Charing Cross Station, Strand, London WC2N 5HS, UK",
    "Covent Garden": "Covent Garden Station, Long Acre, London WC2E 9JT, UK",
    "Earl's Court": "Earl's Court Station, Earl's Court Rd, London SW5 9QA, UK",
    "Edgware Road": "Edgware Road Station, Chapel St, London NW1 5DH, UK",
    "Elephant & Castle": "Elephant & Castle Station, London SE1 6LW, UK",
    "Embankment": "Embankment Station, Villiers St, London WC2N 6NS, UK",
    "Euston": "Euston Station, Euston Rd, London NW1 2RT, UK",
    "Euston Square": "Euston Square Station, Gower St, London NW1 2BU, UK",
    "Farringdon": "Farringdon Station, Cowcross St, London EC1M 6BY, UK",
    "Gloucester Road": "Gloucester Road Station, Gloucester Rd, London SW7 4SF, UK",
    "Goodge Street": "Goodge Street Station, Tottenham Court Rd, London W1T 2HE, UK",
    "Great Portland Street": "Great Portland Street Station, Great Portland St, London W1W 5PP, UK",
    "Green Park": "Green Park Station, Piccadilly, London W1J 9DZ, UK",
    "Holborn": "Holborn Station, Kingsway, London WC2B 6AA, UK",
    "Hyde Park Corner": "Hyde Park Corner Station, Knightsbridge, London SW1X 7TA, UK",
    "King's Cross St. Pancras": "King's Cross St. Pancras Station, Euston Rd, London N1 9AL, UK",
    "Knightsbridge": "Knightsbridge Station, Brompton Rd, London SW1X 7XL, UK",
    "Lambeth North": "Lambeth North Station, Westminster Bridge Rd, London SE1 7PB, UK",
    "Lancaster Gate": "Lancaster Gate Station, Bayswater Rd, London W2 3LG, UK",
    "Leicester Square": "Leicester Square Station, Charing Cross Rd, London WC2H 0AP, UK",
    "Liverpool Street": "Liverpool Street Station, Liverpool St, London EC2M 7QH, UK",
    "London Bridge": "London Bridge Station, London SE1 9SP, UK",
    "Mansion House": "Mansion House Station, Queen Victoria St, London EC4N 4TQ, UK",
    "Marble Arch": "Marble Arch Station, Oxford St, London W1H 7DL, UK",
    "Marylebone": "Marylebone Station, Melcombe Pl, London NW1 6JJ, UK",
    "Monument": "Monument Station, King William St, London EC4R 9AA, UK",
    "Moorgate": "Moorgate Station, Moorgate, London EC2M 6TX, UK",
    "Old Street": "Old Street Station, Old St, London EC1Y 1BE, UK",
    "Oxford Circus": "Oxford Circus Station, Oxford St, London W1B 3AG, UK",
    "Paddington": "Paddington Station, Praed St, London W2 1RH, UK",
    "Piccadilly Circus": "Piccadilly Circus Station, Piccadilly Circus, London W1J 9HP, UK",
    "Pimlico": "Pimlico Station, Bessborough St, London SW1V 2JA, UK",
    "Queensway": "Queensway Station, Queensway, London W2 4SS, UK",
    "Regent's Park": "Regent's Park Station, Marylebone Rd, London NW1 5HA, UK",
    "Russell Square": "Russell Square Station, Bernard St, London WC1N 1LJ, UK",
    "South Kensington": "South Kensington Station, Pelham St, London SW7 2NB, UK",
    "St. James's Park": "St. James's Park Station, Broadway, London SW1H 0BD, UK",
    "St. Paul's": "St. Paul's Station, Cheapside, London EC2V 6AA, UK",
    "Temple": "Temple Station, Victoria Embankment, London WC2R 2PH, UK",
    "Tottenham Court Road": "Tottenham Court Road Station, Oxford St, London W1D 1AN, UK",
    "Tower Hill": "Tower Hill Station, Trinity Square, London EC3N 4DJ, UK",
    "Vauxhall": "Vauxhall Station, Bondway, London SW8 1SJ, UK",
    "Victoria": "Victoria Station, Victoria St, London SW1E 5ND, UK",
    "Warren Street": "Warren Street Station, Tottenham Court Rd, London W1T 5AH, UK",
    "Waterloo": "Waterloo Station, Waterloo Rd, London SE1 8SW, UK",
    "Westminster": "Westminster Station, Bridge St, London SW1A 2JR, UK"
}

# Function to get popular times data
def get_popular_times(address):
    return livepopulartimes.get_populartimes_by_address(address)

# Collect data for each station
data = []
for station, address in stations_with_addresses.items():
    result = get_popular_times(address)
    if result:
        lat = result['coordinates']['lat']
        lng = result['coordinates']['lng']
        popularity = result['current_popularity']
        if isinstance(lat, (int, float)) and isinstance(lng, (int, float)) and isinstance(popularity, (int, float)):
            data.append((lat, lng, popularity))

# Initialize map centered around London
london_map = folium.Map(location=[51.5074, -0.1278], zoom_start=13)

# Add heatmap layer
HeatMap(data, name='Zone 1', min_opacity=0.1, radius=50, blur=50, gradient={0.1: 'blue', 0.5: 'yellow', 1: 'red'}).add_to(london_map)

# Add markers with popularity labels
for lat, lng, popularity in data:
    folium.Marker(
        location=[lat, lng],
        icon=folium.DivIcon(html=f"""<div style="font-family: Arial; color: black; font-size: 12px;">{popularity}</div>""")
    ).add_to(london_map)

# Save map to HTML file
london_map.save("london_heatmap.html")

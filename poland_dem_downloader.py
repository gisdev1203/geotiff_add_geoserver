import requests
from tqdm import tqdm

# Define the bounding box coordinates for Poland in EPSG:2180
bbox = "160827,98927,876030,796522"
resolution = 1

# Calculate the number of tiles based on the resolution
tile_size = 20000  # Adjust this value based on the desired tile size
x_min, y_min, x_max, y_max = map(float, bbox.split(","))
x_tiles = int((x_max - x_min) / tile_size) + 1
y_tiles = int((y_max - y_min) / tile_size) + 1

#open the file in write mode
with open('output.txt', 'w') as file:
    # Generate URLs for each tile and download the data
    for x in tqdm(range(x_tiles), desc="Progress"):
        for y in tqdm(range(y_tiles), desc=f"Downloading Tile {x}"):
            if(x<=11): continue
            if(y<=10): continue
            tile_bbox = "{},{},{},{}".format(
                x_min + (x * tile_size),
                y_min + (y * tile_size),
                x_min + ((x + 1) * tile_size),
                y_min + ((y + 1) * tile_size),
            )
            url = f"https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/GRID1/WCS/DigitalTerrainModelFormatTIFF?service=wcs&request=GetCoverage&version=1.0.0&coverage=DTM_PL-KRON86-NH_TIFF&format=image%2Ftiff&bbox={tile_bbox}&resx={resolution}&resy={resolution}&crs=EPSG%3A2180"
            # response = requests.get(url, stream=True)
            # print(url)
            file.write('\n')
            file.write(f'tile_{x}_{y}.tiff')
            file.write('\n')
            file.write(url)
            file.write('\n')
            # if response.status_code == 200:
            #     filename = f"tile_{x}_{y}.tiff"
            #     with open(filename, "wb") as file:
            #         try:
            #             for chunk in tqdm(response.iter_content(chunk_size=8192), total=1562660):
            #             # for chunk in response.iter_content(chunk_size=8192):
            #                 file.write(chunk)
            #         except requests.exceptions.ChunkedEncodingError:
            #             print(f"ChunkedEncodingError occurred for ({x}, {y}). Retrying...")
            #             response.close()  # Close the previous response
            #             print(f"Failed to download tile ({x}, {y}): {url}")
                        
            # else:
            #     print(f"Failed to download tile ({x}, {y}): {url}")
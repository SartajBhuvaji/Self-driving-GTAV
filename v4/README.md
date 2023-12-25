### Info
- Image Resolution : 270, 480
- Mode : RGB
- Dimension : (270, 480, 3)
- File Count : 100
- Size : 1.81 GB/file
- Total Data Size : 362 GB 

### Data Set sizes
#### Mini : 
- Folder Name : mini
- Files : 01
- Total Size : 1.81 GB
- Total Frames : 5000

#### First Half
- Folder Name : Training Data(1-100)
- Files : 100
- Total Size : 181 GB
- Total Frames : 500,000

#### Second Half
- Folder Name : Training Data(101-200)
- Files : 100
- Total Size : 181 GB
- Total Frames : 500,000

### Data Count
#### Mini
```
 'W':  [1, 0, 0, 0, 0, 0, 0, 0, 0] : 3627
 'S':  [0, 1, 0, 0, 0, 0, 0, 0, 0] : 50
 'A':  [0, 0, 1, 0, 0, 0, 0, 0, 0] : 104
 'D':  [0, 0, 0, 1, 0, 0, 0, 0, 0] : 106
 'WA': [0, 0, 0, 0, 1, 0, 0, 0, 0] : 364
 'WD': [0, 0, 0, 0, 0, 1, 0, 0, 0] : 416
 'SA': [0, 0, 0, 0, 0, 0, 1, 0, 0] : 35
 'SD': [0, 0, 0, 0, 0, 0, 0, 1, 0] : 47
 'NK': [0, 0, 0, 0, 0, 0, 0, 0, 1] : 248
  NONE : 3 
```

#### First Half (Data Count (1-100))
```
 'W':  [1, 0, 0, 0, 0, 0, 0, 0, 0] : 353725
 'S':  [0, 1, 0, 0, 0, 0, 0, 0, 0] : 2243
 'A':  [0, 0, 1, 0, 0, 0, 0, 0, 0] : 14303
 'D':  [0, 0, 0, 1, 0, 0, 0, 0, 0] : 13114
 'WA': [0, 0, 0, 0, 1, 0, 0, 0, 0] : 30877
 'WD': [0, 0, 0, 0, 0, 1, 0, 0, 0] : 29837
 'SA': [0, 0, 0, 0, 0, 0, 1, 0, 0] : 1952
 'SD': [0, 0, 0, 0, 0, 0, 0, 1, 0] : 1451
 'NK': [0, 0, 0, 0, 0, 0, 0, 0, 1] : 52256
  NONE : 242
```
#### Second Half (Data Count (101-200))
```
 'W':  [1, 0, 0, 0, 0, 0, 0, 0, 0] : 359025
 'S':  [0, 1, 0, 0, 0, 0, 0, 0, 0] : 2834
 'A':  [0, 0, 1, 0, 0, 0, 0, 0, 0] : 11025
 'D':  [0, 0, 0, 1, 0, 0, 0, 0, 0] : 9639
 'WA': [0, 0, 0, 0, 1, 0, 0, 0, 0] : 31896
 'WD': [0, 0, 0, 0, 0, 1, 0, 0, 0] : 29756
 'SA': [0, 0, 0, 0, 0, 0, 1, 0, 0] : 1742
 'SD': [0, 0, 0, 0, 0, 0, 0, 1, 0] : 2461
 'NK': [0, 0, 0, 0, 0, 0, 0, 0, 1] : 51313
  NONE : 309
```

### Graphics Details
- Original Resolution : 800 x 600
- Aspect Ratio : 16:10
- All Video Settings : Low

### Camera Details
- Camera : Hood Cam
- Vehical Camera Height : Low
- First Person Vehical Auto-Center : On
- First Person Head Bobbing : Off

### Other Details
- Vehical : Michael's Car
- Vehical Mods : All Max 
- Cv2 Mask : None
- Way Point : Enabled/Following
- Weather Conditions : Mostly Sunny
- Time of Day : Day, Night
- Rain : Some

### Note
- Remove `NONE` while processing the data
- Check `training_data_count_001-100.csv` & `training_data_count_101-200.csv` for detailed count
- Check `training_data_stats.py` for more info
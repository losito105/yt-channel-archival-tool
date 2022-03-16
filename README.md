```
                                    o   o o-O-o o    o         
                                     \ /    |   |    | /       
                                      O     |   O-o  OO   o-o  
                                      |     |   |  | | \  |  | 
                                      o     o   o-o  o  o O-o  
                                                          |    
                                                          o    
 ```
  
Create an archive of your YouTube channel or download videos from others' for offline viewing.

``This application can be run in a Unix command line.``

<h1>Setup</h1>

Install Dependencies:

<table>
  <tr>
    <th>Name</th>
    <th>Version</th>
    <th>Source</th>
  </tr>
  <tr>
    <td>pytube</td>
    <td>v11.0.1</td>
    <td>https://github.com/pytube/pytube</td>
  </tr>
  <tr>
    <td>pip</td>
    <td>v22.0.4</td>
    <td>https://github.com/pypa/pip</td>
  </tr>
  <tr>
    <td>python</td>
    <td>v3.8.2</td>
    <td>https://www.python.org/downloads/source/</td>
  </tr>
   <tr>
    <td>youtube-dl</td>
    <td>v2021.12.17</td>
    <td>https://github.com/ytdl-org/youtube-dl</td>
  </tr>
</table>

- Open a Unix terminal (`macOS` & `Linux`)
- Navigate to a directory where you'd like to clone the repository (see `man cd`)
- Clone this repository into the selected directory (see `man git-clone`)
- Navigate into the the cloned project's directory
- Run `./channel-archival-tool.sh`
- When prompted, enter the name of a YouTube channel
  - Note that spelling & spacing are important here
  - Channel name can be found here: `https://www.youtube.com/c/<channel-name>/videos`

That's it! You are now able to view the download progress of each video as YTbkp executes.

<h1>Additional Features (Coming Soon)</h1>

- The ability to archive or download youtube videos into a specified directory (rather than only the directory within which the bash script was run).
- The ability to select specific videos for download (currently only complete archival of a channel is supported)

<h1>Important Note</h1>

*I do not take credit for writing any of the code included in any of this application's dependencies.*
*This project was created as an exercise in learning* `Vim` *and writing bash scripts and as such does little more than tie existing applications together.*

<h1>Demo</h1>

https://user-images.githubusercontent.com/43625213/158514143-5f74dfbf-dcaa-434d-9daa-9c13d4659b45.mp4

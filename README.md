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

- Open a Unix terminal (macOS & Linux)
- Navigate to a directory where you'd like to clone the repository (see `man cd`)
- Clone this repository into the selected directory (see `man git-clone`)
- Navigate into the the cloned project's directory
- Run `./channel-archival-tool.sh`
- When prompted, enter the name of a YouTube channel
  - Note that spelling & spacing are important here
  - Channel name can be found here: `https://www.youtube.com/c/<channel-name>/videos`
- That's it!

You are now able to view the download progress of each video as YTbkp executes.

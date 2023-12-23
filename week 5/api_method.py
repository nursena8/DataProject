import pandas as pd

def get_channel_stats(youtube,channel_ids):
  all_data=[]
  request=youtube.channels().list(
      part="snippet,contentDetalies,statistics",
      id=",".join(channel_ids)
  )
  response=request.execute()
  for item in response["items"]:
    data={
        "channelNAme":item["snippet"]["title"],
        "subscribers":item["statistics"]["subscriberCount"],"views":item["statistics"]["viewCount"],"totalVideos":item["statistics"]["videoCount"],"playlistId":item["contentDetails"]["relatedPlaylists"]["uploads"]

    }
    all_data.append(data)
  return pd.DataFrame(all_data)
def get_vid_ids(youtube,playlist_id):
  video_ids=[]
  request=youtube.playlistItems().list(
      part="snippet,contentDetails",playlistId=playlist_id,maxResults=50,pageToken=next_page_token


  )
  response=request.execute()
  for item in response["items"]:
    video_ids.append(items["contentDetails"]["videoId"])

  next_page_token = response.get("nextPageToken")
  while next_page_token is not None:
    request=youtube.playlistItems.list(
        part="snippet,contentDetails",playlistId=playlist_id,maxResult=50,pageToken=next_page_token
    )
    response=request.execute()

    for item in response["items"]:
      video_ids.append(item["contentDetails"]["videoId"])

    next_page_token=response.get(next_page_token)
  return video_ids
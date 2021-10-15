
from tokenize import Number
import discord
from discord.ext import commands
import youtube_dl

#queue = []
class music(commands.Cog):
    def _init_(self,client):
        self.client = client




    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Bro, go to a voice channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)




    @commands.command()
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()




    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS ={'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options':'-vn'}
        YDL_OPTIONS = {'format': "bestaudio",
                       'nonplaylist': 'True', 'source_address': '0.0.0.0'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info["formats"][0]['url']
            sauce = discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=URL,
            **FFMPEG_OPTIONS)
            vc.play(sauce)

   # @commands.command()
   # async def queue_(self,ctx, sauce):
   #     global queue
   #     queue.append(sauce)
   #     await ctx.send(f'`{sauce}` added to queue')

   # @commands.command()
   # async def r_q(self,ctx, number):
   #     global queue
        
   #     try:
   #         del(queue[int(number)])
   #         await ctx.send('queue is now `{queue}!`')
   #     except:
   #         await ctx.send('queue is either **empty** or the index is **out of range**')



    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused *.*")
    
    @commands.command()
    async def stop(self,ctx):
        await ctx.voice_client.stop()
        await ctx.send("STOPPED *.*")
    
    
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resuming...")


    
          
def setup(client):
    client.add_cog(music(client))

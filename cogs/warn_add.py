#import discord
#from discord.ext import commands
#import aiosqlite
#import asyncio
#
#class Commands(commands.Cog, name ="Commands"):
#    def __init__(self, bot):
#        self.bot = bot
#
#    @commands.Cog.listener()
#    async def on_command_error(self, ctx, error):
#        pass
#
#    @commands.command()
#    async def addwarn(self, ctx, member : discord.Member, *, reason = None):
#        if member == ctx.author:
#            await ctx.send("Du kannst dich nicht selber warnen!")
#            return
#        if member.bot:
#            await ctx.send("Du kannst keine Bots warnen")
#            return
#        db_name = 'warn.db'
#        db = await aiosqlite.connect(db_name)
#        cursor = await db.cursor()
#
#        await cursor.execute("CREATE TABLE IF NOT EXISTS warn(guild_id STR, user_id STR, warn_num STR, PRIMARY KEY (guild_id, user_id))")
#        await db.commit()
#
#        await cursor.execute("SELECT * FROM warn WHERE guild_id = ? AND user_id = ?", (ctx.guild.id, member.id))
#        data = await cursor.fetchone()
#        if reason == None:
#            reason = "Kein Grund angegeben"
#        if data is None:
#            await cursor.execute("INSERT INTO warn(guild_id, user_id, warn_num) VALUES(?,?,?)", (ctx.guild_id, member.id, str(1)))
#            await db.commit()
#            await ctx.send(f"{member.mention} wurde zum ersten mal gewarnt\nGrund: {reason}")
#            return
#
#        
#        else:
#            await cursor.execute("UPDATE warn SET warn_num = warn_num + ? WHERE guild_id = ? AND user_id = ?", (str(1), ctx.guild.id, ctx.author, member.id))
#            await db.commit()
#            await cursor.execute("SELECT warn_num FROM warn WHERE guild_id = ? AND user_id = ?", (ctx.guild.id, member.id))
 ##           data2 = await cursor.fetchone("")
 #           final = data2[0]
  #          print(final)
  ##          await ctx.send(f"{member.mention} wurde gewarnt {final}\nGrund: {reason}")
  #          return

#def setup(bot):
#    bot.add_cog(Commands(bot))
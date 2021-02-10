import sys
print(sys.executable)
import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!what do ra'):
            await message.channel.send('I do pilli pilli'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!likethismeanshowra'):
            await message.channel.send(':imseeing:'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!saji'):
            await message.channel.send('What ra chettha fellow '.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!imseeing'):
            await message.channel.send('Eyes, I will pull it out'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!chettha pilli'):
            await message.channel.send('s'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!goodu coffee'):
            await message.channel.send('bery tasty ra it is'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!chettha oryon'):
            await message.channel.send('I ple gheims '.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!gib milk'):
            await message.channel.send(' pilli wants milk aa ?'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!realize'):
            await message.channel.send('You left me alone aa?'.format(message))
        if message.author.id == self.user.id:
            return 
        if message.content.startswith('!what do ra'):
            await message.chanel.send('I do pilli pilli'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!goodu pilli'):
            await.message.channel.send('pilli should get milk'.format(message))
 client = MyClient()
 client.run('token')
        
       

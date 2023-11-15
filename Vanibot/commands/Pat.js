const Discord = require('discord.js');
module.exports = {
    name: 'Pat',
    description: "Pats the user!",
    execute(message, args){
        if (args[0] != undefined && args[0][0] == "<") {
            const patEmbed = new Discord.MessageEmbed()
                .setColor('#ff8800')
                .setTitle("You've been patted!")
                .setURL('https://cdn.weeb.sh/images/H1MIei2AZ.gif')
                .setImage('https://cdn.weeb.sh/images/H1MIei2AZ.gif');
            //message.channel.send("*Pats* " + args[0]);
            //message.channel.send("https://cdn.weeb.sh/images/H1MIei2AZ.gif")
            message.channel.send(patEmbed);
            console.log(JSON.stringify(args));
        } else {
            message.channel.send("Who you wanna pat tho?")
        }
    }
}
const Discord = require('discord.js');
const { prefix } = require('./config.json');
const token = process.env.TOKEN
const client = new Discord.Client();
const { c, MessageEmbed } = require("discord.js")
client.once('ready', () => {
    console.log('Ready!')
})
client.on('message', message => {
    if (!message.content.startsWith(prefix) || message.author.bot) return;
    const args = message.content.slice(prefix.length).split(' ');
    const command = args.shift().toLowerCase();

    // using the new `command` variable, this makes it easier to manage!
    // you can switch your other commands to this format as well
    if (command === 'help') {
        if (!args.length) {
            const helpEmbed = new MessageEmbed
            helpEmbed
                .setColor(`#006fff`)
                .setTimestamp(message.createdTimestamp)
                .setTitle("COMMANDS:")
                .setDescription(
                    `${prefix}kick - \`{${prefix}kick [MentionUser]}\``,
                    `${prefix}ban  - \`{${prefix}ban [MentionUser]}\``
                )
        }
        return message.channel.send(`NOOB, ${message.author}!`);
    }
    if(message.member.hasPermission(["KICK_MEMBERS", "BAN_MEMBERS", "ADMINISTRATOR"])) {
        if(command === 'kick') {
            if (!args.length) {

            }
            const helpEmbed = new MessageEmbed
            helpEmbed
                .setColor(`#006fff`)
                .setTimestamp(message.createdTimestamp)
                .setTitle("COMMANDS:")
                .setDescription(
                    `${prefix}kick - \`{${prefix}kick [MentionUser]}\``,
                    `${prefix}ban  - \`{${prefix}ban [MentionUser]}\``
                )
                channel.message.send(helpEmbed);
        }
    }
})
client.login(token);

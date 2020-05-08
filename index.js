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
                message.channel.send(helpEmbed)
        }
        return
    }
    if(message.member.hasPermission(["KICK_MEMBERS", "BAN_MEMBERS", "ADMINISTRATOR"])) {
        if(command === 'kick') {
            if (!args.length) {
                let member1 = args(user)
                let member2 = message.mentions.members.first()
                let member3 = args(user.tag)
                [member1, member2, member3].kick().then((message) => {
                const helpEmbed2 = new MessageEmbed
                helpEmbed2
                    .setColor(`#07ff00`)
                    .setTimestamp(message.createdTimestamp)
                    .setTitle("SUCCESS")
                    .setDescription(
                        `\:white_check_mark: ***${member.user} has been banned!***`
                    )
                    message.channel.send(helpEmbed2);
                }).catch((err) => {
                    
                });
            }
            const helpEmbed1 = new MessageEmbed
            helpEmbed1
                .setColor(`#ff0000`)
                .setTimestamp(message.createdTimestamp)
                .setTitle("INVALID USAGE")
                .setDescription(
                    `\:warning: ***Invalid usage of __kick__ command***`
                )
                message.channel.send(helpEmbed1);
        }
    }
})
client.login(token);

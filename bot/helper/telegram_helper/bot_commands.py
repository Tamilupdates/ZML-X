#!/usr/bin/env python3
from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand       = 'start'
        self.MirrorCommand      = [f'mirror{CMD_SUFFIX}',    f'm{CMD_SUFFIX}']
        self.QbMirrorCommand    = [f'qbmirror{CMD_SUFFIX}',  f'qm{CMD_SUFFIX}']
        self.YtdlCommand        = [f'watch{CMD_SUFFIX}',     f'w{CMD_SUFFIX}']
        self.LeechCommand       = [f'leech{CMD_SUFFIX}',     f'l{CMD_SUFFIX}']
        self.QbLeechCommand     = [f'qbleech{CMD_SUFFIX}',   f'ql{CMD_SUFFIX}']
        self.YtdlLeechCommand   = [f'leechwatch{CMD_SUFFIX}',f'lw{CMD_SUFFIX}']
        self.CancelAllCommand   = [f'cancelall{CMD_SUFFIX}', f'ca{CMD_SUFFIX}']
        self.RestartCommand     = [f'restart{CMD_SUFFIX}',   f'rst{CMD_SUFFIX}']
        self.StatusCommand      = [f'status{CMD_SUFFIX}',    f'sts{CMD_SUFFIX}']
        self.PingCommand        = [f'ping{CMD_SUFFIX}',      f'p{CMD_SUFFIX}']
        self.StatsCommand       = [f'stats{CMD_SUFFIX}',     f's{CMD_SUFFIX}']
        self.CloneCommand       = f'clone{CMD_SUFFIX}'
        self.CountCommand       = f'count{CMD_SUFFIX}'
        self.DeleteCommand      = f'del{CMD_SUFFIX}'
        self.CancelMirror       = f'cancel{CMD_SUFFIX}'
        self.ListCommand        = [f'list{CMD_SUFFIX}',     f'ls{CMD_SUFFIX}']
        self.SearchCommand      = f'search{CMD_SUFFIX}'
        self.UsersCommand       = f'usr{CMD_SUFFIX}'
        self.AuthorizeCommand   = f'au{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'un{CMD_SUFFIX}'
        self.AddSudoCommand     = f'asd{CMD_SUFFIX}'
        self.RmSudoCommand      = f'rmsd{CMD_SUFFIX}'
        self.HelpCommand        = f'help{CMD_SUFFIX}'
        self.LogCommand         = f'log{CMD_SUFFIX}'
        self.ShellCommand       = f'shell{CMD_SUFFIX}'
        self.EvalCommand        = f'eval{CMD_SUFFIX}'
        self.ExecCommand        = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand      = f'bst{CMD_SUFFIX}'
        self.UserSetCommand     = f'usetting{CMD_SUFFIX}'
        self.BtSelectCommand    = f'btsel{CMD_SUFFIX}'
        self.RssCommand         = f'rss{CMD_SUFFIX}'
        self.CategorySelect     = f'catsel{CMD_SUFFIX}'
        self.RmdbCommand        = f'rmdb{CMD_SUFFIX}'
        self.RmalltokensCommand = f'rmat{CMD_SUFFIX}'

BotCommands = _BotCommands()

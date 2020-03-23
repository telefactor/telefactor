from textwrap import dedent as dd


import click


def echo(*msgs):
    click.echo(fmt_msgs(msgs))


def echo_info(*msgs):
    click.secho(fmt_msgs(msgs), fg="yellow")


def fmt_msgs(msgs):
    """
    Handles lines and indentation!

        cli.echo(
           '''
              line
                 indented
           ''',
           'inline',
           '   inline indented',
           '''
           different indent
           '''
        )

    Output:
        line
              indented

        inline
           inline indented

        different indent
    """
    return str.strip(dd("\n".join(msgs)))


def definition_list(rows: "[(str, str)]") -> str:
    return "\n".join(
        f"{title:{'·' if i % 2 == 0 else ' '}<15}{value}"
        for i, (title, value) in enumerate(rows)
    )

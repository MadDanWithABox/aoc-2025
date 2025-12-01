"""
Advent of Code wrapper module for running daily solutions.

    from ..wrapper import aoc_runner
    
    def part1(input_data: str | None) -> int:
        # If input_data is None, use your test data
        if input_data is None:
            input_data = "your test data here"
        # Your solution here
        return result
    
    def part2(input_data: str | None) -> int:
        # Your solution here
        return result
    
    if __name__ == "__main__":
        aoc_runner(part1, part2)
"""

from pathlib import Path
from typing import Callable, Optional
import typer


def aoc_runner(
    part1_func: Callable[[str], any],
    part2_func: Optional[Callable[[str], any]] = None,
):
    """
    Create a Typer CLI app for running Advent of Code solutions.
    
    Args:
        part1_func: Function that takes input string and returns part 1 solution
        part2_func: Function that takes input string and returns part 2 solution
    """
    app = typer.Typer()
    
    @app.command()
    def run(
        part: int = typer.Argument(..., help="Which part to run (1 or 2)"),
        input_file: Optional[Path] = typer.Option(
            None,
            "--input", "-i",
            help="Path to input file (if not provided, uses test data)",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
        ),
    ):
        """Run the specified part of the Advent of Code solution."""
        
        # Validate part number
        if part not in [1, 2]:
            typer.echo("Error: part must be 1 or 2", err=True)
            raise typer.Exit(1)
        
        # Check if part 2 function exists
        if part == 2 and part2_func is None:
            typer.echo("Error: part2 function not implemented", err=True)
            raise typer.Exit(1)
        
        # Read input file or use None for test data
        input_data = None
        if input_file is not None:
            try:
                input_data = input_file.read_text().strip()
                typer.echo(f"Using input from: {input_file}")
            except Exception as e:
                typer.echo(f"Error reading input file: {e}", err=True)
                raise typer.Exit(1)
        else:
            typer.echo("Using test data")
        
        # Run the appropriate part
        func = part1_func if part == 1 else part2_func
        
        try:
            result = func(input_data)
            typer.echo(f"Part {part} result: {result}")
        except Exception as e:
            typer.echo(f"Error running part {part}: {e}", err=True)
            raise typer.Exit(1)
    
    app()
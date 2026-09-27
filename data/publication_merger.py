from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent
    in_dir = base_dir / "publications"
    out_file = base_dir / "publications.yml"

    year_dirs = sorted(
        (path for path in in_dir.iterdir()
         if path.is_dir() and not path.name.startswith(".")),
        key=lambda path: path.name,
        reverse=True,
    )

    # Build the complete output before replacing the existing file.
    lines = []
    for year_dir in year_dirs:
        yml_files = sorted(
            (path for path in year_dir.glob("*.yml")
             if path.is_file() and not path.name.startswith(".")),
            key=lambda path: path.name,
            reverse=True,
        )
        if not yml_files:
            continue

        lines.append(f"  - year: {year_dir.name}")
        lines.append("    papers:")
        for yml_file in yml_files:
            content = yml_file.read_text(encoding="utf-8")
            if not content.strip():
                raise ValueError(f"Empty publication file: {yml_file}")
            print(yml_file.stem)
            lines.append(f"      - name: {yml_file.stem}")
            lines.extend(f"        {line}" for line in content.splitlines())

    header = "years:" if lines else "years: []"
    output = "\n".join([header, *lines]) + "\n"
    out_file.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()

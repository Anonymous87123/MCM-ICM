from __future__ import annotations

import close_q99_transaction as base


PAPER_ID = "P-B-2013-21185-c7f22f59"


def main() -> None:
    base.PAPER_ID = PAPER_ID
    base.main()


if __name__ == "__main__":
    main()

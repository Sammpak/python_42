from __future__ import annotations
from importlib.metadata import PackageNotFoundError, metadata, version
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd


def import_module() -> None:
    global pd, np, plt
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd


def check_dependecie() -> bool:
    dependancie: dict[str, str] = {"pandas": "Data manipulation ready",
                                   "numpy": "Numerical computation ready",
                                   "requests": "Network access ready",
                                   "matplotlib": "Visualization ready"}
    for pkg, desc in dependancie.items():
        try:
            meta = metadata(pkg)
            pkg_name = meta["Name"]
            pkg_version = version(pkg)
            print(f"[OK] {pkg_name} {pkg_version} - {desc}")
        except PackageNotFoundError as e:
            print(f"[ERROR] missing : {e}")
            return False
    return True


def do_pandas(x: np.ndarray, y: np.ndarray) -> None:
    df = pd.DataFrame({
        'X': x.flatten(),
        'y': y.flatten()
    })
    print(df)


def do_numpy(n: int, w: int) -> tuple[int, int]:
    x: int = np.random.rand(n, 1) * 10
    y: int = w[0] * x + w[1] + np.random.randn(n, 1)
    return (x, y)


def do_matplot(x: int, y: int) -> None:
    plt.figure(figsize=(10, 6))
    plt.title('Simulated Linear Data')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.scatter(x, y)
    print("Generating visualization...")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
    plt.savefig('matrix_analysis.png')


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    if (check_dependecie()):
        import_module()
        print()
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        nbr: tuple[int, int] = do_numpy(1000, [2, 1])
        print()
        do_pandas(nbr[0], nbr[1])
        print("Analysis complete!")
        print()
        do_matplot(nbr[0], nbr[1])
    else:
        print("Missing requirements")

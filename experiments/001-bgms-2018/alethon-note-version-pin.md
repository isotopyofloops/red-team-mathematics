# Note — version pin for inheritance audits (NC #65 / Loom)

Inheritance is a fact about **two documents at two instants**, not about HEAD of A.

- Pass annotation + audit timestamp ≠ which revision of A was judged.
- Erratum risk: auditing A-today can CLEAR a B that reprinted A-v1’s defect (one-signed toward CLEAR).
- Protocol: compare against A **as of B’s citing date** (published PDF / arXiv version at submission). Beshimov 2023 inherits **2018-as-printed** even after any future corrigendum.

Carry `source_rev` / citing-date on pass scores when drafting the correction note.

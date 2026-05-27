"""
Công cụ trích xuất nội dung text từ file PDF (slides bài giảng).

Cách dùng:
    python tools/extract_pdf.py <đường_dẫn_pdf> [--pages 1,3,5-10]

Ví dụ:
    python tools/extract_pdf.py "Slides/08-Thiet ke kien truc_DA modified.pdf"
    python tools/extract_pdf.py "Slides/06_Quy trình thu thập yêu cầu.pdf" --pages 5-12
"""

import argparse
import sys
import io
from pathlib import Path

# Fix encoding cho Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: Cần cài thư viện PyMuPDF. Chạy: pip install pymupdf")
    sys.exit(1)


def parse_page_ranges(page_str: str, max_page: int) -> list[int]:
    """Phân tích chuỗi page range như '1,3,5-10' thành danh sách số trang (0-indexed)."""
    pages = []
    for part in page_str.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            start = max(1, int(start))
            end = min(max_page, int(end))
            pages.extend(range(start - 1, end))
        else:
            p = int(part)
            if 1 <= p <= max_page:
                pages.append(p - 1)
    return sorted(set(pages))


def extract_text(pdf_path: str, pages: list[int] | None = None) -> None:
    """Trích xuất và in text từ file PDF theo từng trang."""
    doc = fitz.open(pdf_path)
    total = len(doc)

    if pages is None:
        pages = list(range(total))

    print(f"=== File: {Path(pdf_path).name} | Tổng số trang: {total} ===\n")

    for page_num in pages:
        if page_num >= total:
            continue
        page = doc[page_num]
        text = page.get_text("text").strip()

        print(f"--- Trang {page_num + 1}/{total} ---")
        if text:
            print(text)
        else:
            print("[Trang này chỉ chứa hình ảnh, không có text trích xuất được]")

        # Liệt kê các ảnh trong trang (nếu có)
        images = page.get_images(full=True)
        if images:
            print(f"  [Trang này có {len(images)} hình ảnh nhúng]")

        print()

    doc.close()


def main():
    parser = argparse.ArgumentParser(description="Trích xuất text từ file PDF")
    parser.add_argument("pdf_path", help="Đường dẫn đến file PDF")
    parser.add_argument(
        "--pages",
        help="Các trang cần trích xuất, ví dụ: 1,3,5-10. Mặc định: tất cả",
        default=None,
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        print(f"ERROR: Không tìm thấy file: {pdf_path}")
        sys.exit(1)

    # Xác định danh sách trang
    page_list = None
    if args.pages:
        doc = fitz.open(str(pdf_path))
        page_list = parse_page_ranges(args.pages, len(doc))
        doc.close()

    extract_text(str(pdf_path), page_list)


if __name__ == "__main__":
    main()

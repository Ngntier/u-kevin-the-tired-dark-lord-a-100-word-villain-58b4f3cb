import os
TEXT = "Come in. Mind the step. I had it loosened myself, when the guards still saluted. Sit. Not there. That chair was my brother's, and the cushion remembers him better than I do. You came for the crown. It sits in the chapel, under seven locks, and the key\u2014 hmm. The key is in my pocket. Eleven years now. Here is my offer, hero. Take the scepter, the treasury, the ravens, the whole damp castle. Leave me the library, the kettle, and one quiet hour before supper. Refuse, and I will get up. Slowly. Then we shall see who blinks first."
def main():
    assert 95 <= len(TEXT.split()) <= 105 and 1 <= len(TEXT) <= 600
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
if __name__ == "__main__":
    main()

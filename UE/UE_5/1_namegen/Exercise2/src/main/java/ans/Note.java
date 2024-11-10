package ans;

public class Note {
    private int noteId;
    private String title;
    private String content;

    public Note() {
    }

    public Note(String noteId, String title, String content) {
        this(Integer.parseInt(noteId), title, content);
    }

    public Note(int noteId, String title, String content) {
        this.noteId = noteId;
        this.title = title;
        this.content = content;
    }

    public int getNoteId() {
        return noteId;
    }

    public void setNoteId(int noteId) {
        this.noteId = noteId;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
}
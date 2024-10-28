package notes;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NoteController {
    private static List<Note> notes = new ArrayList<Note>();

    @RequestMapping(value = "/note", method = RequestMethod.GET)
    public List<Note> note() {
        return notes;
    }

    @RequestMapping(value = "/note", method = RequestMethod.POST)
    public void note(@RequestBody Note note) {
        notes.add(note);
    }
}
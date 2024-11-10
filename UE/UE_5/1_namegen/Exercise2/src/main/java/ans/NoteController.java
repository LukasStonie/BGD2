package ans;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;

@RestController
public class NoteController {
    private static Jedis jedis = new JedisPool(System.getenv("REDIS_HOST"), 6379).getResource();
    private static int count = 0;

    @RequestMapping(value = "/note", method = RequestMethod.GET)
    public List<Note> note() {
        List<Note> notes = new ArrayList<Note>();

        for (int i = 0; i < count; i++) {
            Map<String, String> noteMap = jedis.hgetAll("note" + i);
            notes.add(new Note(noteMap.get("noteId"), noteMap.get("title"), noteMap.get("content")));
        }

        return notes;
    }

    @RequestMapping(value = "/note", method = RequestMethod.POST)
    public void note(@RequestBody Note note) {
        Map<String, String> newNote = new HashMap<String, String>();
        newNote.put("noteId", Integer.toString(note.getNoteId()));
        newNote.put("title", note.getTitle());
        newNote.put("content", note.getContent());

        jedis.hmset("note" + count, newNote);
        count++;
    }
}
import { useState, useEffect } from 'react'
import { ListItem } from '../components'

const NotesListPage = () => {
    const [notes, setNotes] = useState([])

    const getNotes = async () => {
        const response = await fetch("http://127.0.0.1:8000/api/notes")
        const data = await response.json()
        console.info(data)
        setNotes(data)
    }

    useEffect(() => {
        getNotes()
    }, [])
    return (
        <div>
            <div className='notes-list'>
                {notes.map((note, i) => (
                    <div key={i}>
                        <ListItem note={note}/>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default NotesListPage
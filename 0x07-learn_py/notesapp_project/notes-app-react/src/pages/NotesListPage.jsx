import { useState, useEffect } from 'react'
import { ListItem, AddButton } from '../components'

const NotesListPage = () => {
    const [notes, setNotes] = useState([])

    const getNotes = async () => {
        const response = await fetch("/api/notes/")
        const data = await response.json()
        // console.info(data)
        setNotes(data)
    }

    useEffect(() => {
        getNotes()
    }, [])
    return (
        <div className='notes'>
            <div className='notes-header'>
                <h2 className='notes-title'> &#9782; Notes</h2>
                <p className='notes-count'> {notes.length}</p>
            </div>
            <div className='notes-list'>
                {notes.map((note, i) => (
                    <div key={i}>
                        <ListItem note={note}/>
                    </div>
                ))}
            </div>
            <AddButton/>
        </div>
    )
}

export default NotesListPage
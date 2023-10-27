import { useState, useEffect } from 'react'
// import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'
import arrowLeft from "../assets/arrow-left.svg"
import Image from 'next/image'


const NotePage = ({ match, history }) => {
    const noteId = match.params.id
    const [note, setNote] = useState(null)

    const createNote = async () => {
        const response = await fetch(`/api/notes/`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(note),
        })
        // const data = await response.json()
    }

    const getNote = async () => {
        if(noteId==="new") return
        const response = await fetch(`/api/notes/${noteId}/`)
        const data = await response.json()
        setNote(data)
    }

    const updateNote = async () => {
        const response = await fetch(`/api/notes/${noteId}/`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(note),
        })
        // const data = await response.json()
    }

    const deleteNote = async () => {
        const response = await fetch(`/api/notes/${noteId}/`, {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json',
            },
        })
        // const data = await response.json()
        history.push("/")
    }

    const handleSubmit = () => {
        if(noteId!=="new" && note.body===""){
            deleteNote()
        } else if (noteId!=="new"){
            updateNote()
        } else if (noteId==="new" && note.body!==null){
            createNote()
        }
        history.push("/")
    }

    const handleChange = (val) => {
        setNote(note => ({...note, body: val}))
    }

    useEffect(() => {
        getNote()
    }, [noteId])
    return (
        <div className='note'>
            <div className='note-header'>
                <h3>
                    {/* <ArrowLeft onClick={handleSubmit} /> */}
                    <div onClick={handleSubmit}>
                    <Image
                        src={arrowLeft}
                        alt='arrow-left'
                        width={24}
                        height={24}
                    />
                    </div>
                </h3>
                {noteId !== "new" ? (
                    <button onClick={deleteNote}>
                        Delete
                    </button>
                ) : (
                    <button onClick={handleSubmit}>
                        Done
                    </button>
                )}
            </div>
            <textarea
                onChange={(e) => handleChange(e.target.value)}
                value={note?.body}
            ></textarea>
        </div>
    )
}

export default NotePage
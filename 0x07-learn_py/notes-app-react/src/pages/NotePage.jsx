import { useState, useEffect } from 'react'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'
import { Link } from 'react-router-dom'

const NotePage = ({ match }) => {
    const noteId = match.params.id
    const [note, setNote] = useState(null)

    const getNote = async () => {
        const response = await fetch(`/api/notes/${noteId}/`)
        const data = await response.json()
        setNote(data)
    }

    useEffect(() => {
        getNote()
    }, [noteId])
    return (
        <div className='note'>
            <div className='note-header'>
                <h3>
                    <Link to="/">
                        <ArrowLeft />
                    </Link>
                </h3>
            </div>
            <textarea defaultValue={note?.body}></textarea>
        </div>
    )
}

export default NotePage
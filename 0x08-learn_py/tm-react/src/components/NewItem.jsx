import {useContext} from 'react'
import { TaskContext } from '../context/taskContext'

const NewItem = ({ item }) => {
    const {viewCompleted} = useContext(TaskContext)
    return (
        <>
            <li
                key={item.id}
                className='list-group-item d-flex justify-content-between align-items-center'
            >
                <span
                    className={`todo-title mr-2 ${viewCompleted ? "completed-todo" : ""}`}
                    title={item.title}
                >
                    {item.title}
                </span>
                <span>
                    <button className='btn btn-info mr-2'>
                        Edit
                    </button>
                    <button className='btn btn-danger mr-2'>
                        Delete
                    </button>
                </span>
            </li>
        </>
    )
}

export default NewItem
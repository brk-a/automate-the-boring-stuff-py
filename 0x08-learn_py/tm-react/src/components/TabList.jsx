import {useContext} from 'react'
import { TaskContext } from '../context/taskContext'

const TabList = () => {
    const {
        displayCompleted,
        viewCompleted,
        setDisplayCompleted
    } = useContext(TaskContext)
  return (
    <div>
        {displayCompleted ? (
        <div className='my-5 tab-list'>
          <span
            onClick={() => setDisplayCompleted(true)}
            className={viewCompleted ? "active" : ""}
          >
            Complete
          </span>
        </div>
      ) : (
        <span
            onClick={() => setDisplayCompleted(false)}
            className={viewCompleted ? "" : "active"}
          >
            Incomplete
          </span>
      )}
    </div>
  )
}

export default TabList
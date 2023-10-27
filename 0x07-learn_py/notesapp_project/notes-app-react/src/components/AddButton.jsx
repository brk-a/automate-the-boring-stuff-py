import { Link } from 'react-router-dom'
import Image from 'next/image'
import addButton from "../assets/add.svg"

const AddButton = () => {
  return (
    <Link to="/note/new" className='floating-button'>
        <Image
            src={addButton}
            alt='add-button'
            width={24}
            height={24}
        />
    </Link>
  )
}

export default AddButton
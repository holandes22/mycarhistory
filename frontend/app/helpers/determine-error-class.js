export default function(error) {
    return (error.status === 404) ? 'info' : 'danger';
}


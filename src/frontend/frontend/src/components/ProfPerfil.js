export default function ProfPerfil({prof}){
    return (
        <>
        <h1>{prof.nome}</h1>
        <img 
            className="avatar"
            src={prof.imageUrl}
            alt={'Photo of' + prof.nome}
            style={{width: 90, height: 90}}
        />
        </>
    );
}
import snapshot from "../generated/schedule.json";

export function GET() {
  return Response.json(snapshot);
}
